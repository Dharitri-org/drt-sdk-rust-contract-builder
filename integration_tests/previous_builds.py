
from typing import Dict, List, Optional



class PreviousBuild:
    def __init__(self, name: str,
                 project_archive_url: Optional[str],
                 project_relative_path_in_archive: Optional[str],
                 packaged_src_url: Optional[str],
                 contract_name: Optional[str],
                 expected_code_hashes: Dict[str, str],
                 docker_image: str) -> None:
        self.name = name
        self.project_zip_url = project_archive_url
        self.project_relative_path_in_archive = project_relative_path_in_archive
        self.packaged_src_url = packaged_src_url
        self.contract_name = contract_name
        self.expected_code_hashs = expected_code_hashes
        self.docker_image = docker_image


previous_builds: List[PreviousBuild] = [
    PreviousBuild(
        name="a.1",
        project_archive_url="https://github.com/Dharitri-org/drt-exchange-sc/archive/refs/tags/v0.0.2.zip",
        project_relative_path_in_archive="drt-exchange-sc-v0.0.2",
        packaged_src_url=None,
        contract_name=None,
        expected_code_hashes={
            "farm-staking": "6dc7c587b2cc4b177a192b709c092f3752b3dcf9ce1b484e69fe64dc333a9e0a",
            "farm": "931ca233826ff9dacd889967365db1cde9ed8402eb553de2a3b9d58b6ff1098d",
            "factory": "df06465b651594605466e817bfe9d8d7c68eef0f87df4a8d3266bcfb1bef6d83",
            "pair": "f3f08ebd758fada871c113c18017d9761f157d00b19c4d3beaba530e6c53afc2",
            "energy-factory": "241600c055df605cafd85b75d40b21316a6b35713485201b156d695b23c66a2f"
        },
        docker_image="dharitriorg/sdk-rust-contract-builder:next"
    ),
    PreviousBuild(
        name="a.2",
        project_archive_url="https://github.com/Dharitri-org/drt-metabonding-sc/archive/refs/tags/v1.1.1.zip",
        project_relative_path_in_archive="drt-metabonding-sc-v1.1.1",
        packaged_src_url=None,
        contract_name=None,
        expected_code_hashes={
            "metabonding": "897b19e1990f7c487c99c12f50722febe1ee4468bcd3a7405641966dfff2791d"
        },
        docker_image="dharitriorg/sdk-rust-contract-builder:next"
    ),
    PreviousBuild(
        name="a.3",
        project_archive_url="https://github.com/Dharitri-org/drt-contract-rs/archive/refs/tags/v0.0.1.zip",
        project_relative_path_in_archive="drt-contract-rs-0.0.1",
        packaged_src_url=None,
        contract_name=None,
        expected_code_hashes={
            "adder": "384b680df7a95ebceca02ffb3e760a2fc288dea1b802685ef15df22ae88ba15b",
            "multisig": "5a8ed9e5b9ad81ffa4109262f5482e8ebc10dba339e61e992b5a7501f8e22bd5",
            "multisig-full": "88e1a67b630cd8efdee8ce6254322f4d7dda6c723a5c33e5a1e890ff9713e290",
            "multisig-view": "bfdc84983ab9615e7859da9f3815b6189dd315437ade767f87615ca9ba625397",
            "lottery-dct": "d90f13fcc50108de89b629ca6bfdd7ba378c172a19488c56a97ab571cb6160e2"
  
        },
        docker_image="dharitriorg/sdk-rust-contract-builder:next"
    ),
    PreviousBuild(
        name="a.4",
        project_archive_url="https://github.com/Dharitri-org/drt-contract-rs/archive/refs/tags/v0.0.1.zip",
        project_relative_path_in_archive="drt-contract-rs-0.0.1",
        packaged_src_url=None,
        contract_name=None,
        expected_code_hashes={
            "adder": "384b680df7a95ebceca02ffb3e760a2fc288dea1b802685ef15df22ae88ba15b",
            "multisig": "5a8ed9e5b9ad81ffa4109262f5482e8ebc10dba339e61e992b5a7501f8e22bd5",
            "multisig-full": "f6b5457682b39ea1bd52fd6fe293257a3d5a5bb931c9e404c9ba24617cd51438",
            "multisig-view": "88e1a67b630cd8efdee8ce6254322f4d7dda6c723a5c33e5a1e890ff9713e290",
            "lottery-dct": "bfdc84983ab9615e7859da9f3815b6189dd315437ade767f87615ca9ba625397",
            "ping-pong-moax": "d90f13fcc50108de89b629ca6bfdd7ba378c172a19488c56a97ab571cb6160e2"
        },
        docker_image="sdk-rust-contract-builder:next"
    ),
]
