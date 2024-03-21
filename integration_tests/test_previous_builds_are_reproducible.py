import json
import shutil
import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import List, Optional, Tuple
import traceback

from integration_tests.config import (CARGO_TARGET_DIR, DOWNLOADS_FOLDER,
                                      EXTRACTED_FOLDER, PARENT_OUTPUT_FOLDER)
from integration_tests.previous_builds import PreviousBuild, previous_builds
from integration_tests.shared import (download_packaged_src,
                                      download_project_repository, run_docker)


def main(cli_args: List[str]):
    try:
        parser = ArgumentParser()
        parser.add_argument("--selected-builds", nargs='+')
        parsed_args = parser.parse_args(cli_args)
        selected_builds = parsed_args.selected_builds

        shutil.rmtree(DOWNLOADS_FOLDER, ignore_errors=True)
        shutil.rmtree(EXTRACTED_FOLDER, ignore_errors=True)
        shutil.rmtree(PARENT_OUTPUT_FOLDER, ignore_errors=True)

        DOWNLOADS_FOLDER.mkdir(parents=True, exist_ok=True)
        EXTRACTED_FOLDER.mkdir(parents=True, exist_ok=True)
        CARGO_TARGET_DIR.mkdir(parents=True, exist_ok=True)

        for build in previous_builds:
            if not build.name in selected_builds:
                continue

            print("Reproducing build", build.name, "...")
            try:
                project_path, packaged_src_path = fetch_source_code(build)
                output_folder = PARENT_OUTPUT_FOLDER / build.name
                output_folder.mkdir(parents=True, exist_ok=True)

                if project_path and build.project_relative_path_in_archive:
                    project_path = project_path / build.project_relative_path_in_archive

                run_docker(
                    project_path=project_path,
                    packaged_src_path=packaged_src_path,
                    contract_name=build.contract_name,
                    image=build.docker_image,
                    output_folder=output_folder)

                check_code_hashes(build, output_folder)
            except Exception as e:
                print(f"Error reproducing build {build.name}: {str(e)}")
                traceback.print_exc()  
    except Exception as e:
                print(f"Error reproducing build {build.name}: {str(e)}")
                traceback.print_exc() 


def fetch_source_code(build: PreviousBuild) -> Tuple[Optional[Path], Optional[Path]]:
    print("Fetching source code for", build.name, "...")
    try:
        if build.project_zip_url:
            print(f" build.project_src_url: {list(build)}")
            return download_project_repository(build.project_zip_url, build.name), None
        if build.packaged_src_url:
            print(f" build.packaged_src_url: {build}")
            return None, download_packaged_src(build.packaged_src_url, build.name)
    except Exception as e:
            print(f"fetch_source_code {build.name}: {str(e)}")
            traceback.print_exc()  # Print detailed traceback information
    raise Exception("No source code provided")


def check_code_hashes(build: PreviousBuild, output_folder: Path):
    try:
        artifacts_path = output_folder / "artifacts.json"
        artifacts_json = artifacts_path.read_text()
        artifacts = json.loads(artifacts_json)

        for contract_name, expected_code_hash in build.expected_code_hashs.items():
            print(f"For contract {contract_name}, expecting code hash {expected_code_hash} ...")

            try:
                codehash = artifacts["contracts"][contract_name]["codehash"]
            except KeyError:
                # Handle "artifacts.json" created by older images
                codehash = artifacts[contract_name]["codehash"]
            if codehash != expected_code_hash:
                raise Exception(f"{build.name}: codehash mismatch for contract {contract_name}! Expected {expected_code_hash}, got {codehash}")
            print("OK, codehashes match:", codehash)
    except Exception as e:
            print(f"check_code_hashes {build.name}: {str(e)}")
            traceback.print_exc()  # Print detailed traceback information


if __name__ == "__main__":
    main(sys.argv[1:])
