# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from os import environ
from dataclasses import dataclass, field, asdict


@dataclass
class Config:
    github_token: str               = field(default_factory=lambda: environ.get('GITHUB_TOKEN', ''))
    github_name: str                = field(default_factory=lambda: environ.get('GITHUB_NAME', ''))
    github_email: str               = field(default_factory=lambda: environ.get('GITHUB_EMAIL', ''))
    provider_api_key: str           = field(default_factory=lambda: environ.get('PROVIDER_API_KEY', ''))
    provider: str                   = field(default_factory=lambda: environ.get('PROVIDER', ''))
    machine_organization_name: str  = field(default_factory=lambda: environ.get('ORGANIZATION_NAME', 'machina-ratiocinatrix'))
    private_repo_with_text: str     = field(default_factory=lambda: environ.get('REPO_WITH_INSTRUCTIONS','machina_ratiocinatrix'))
    system_prompt_file: str         = field(default_factory=lambda: environ.get('SYSTEM_INSTRUCTIONS_FILE', 'machina.yaml'))
    name: str                       = field(default_factory=lambda: environ.get('NAME', ''))
    instructions: str               = field(default_factory=lambda: environ.get('INSTRUCTIONS', ''))
    verb: str                       = field(default_factory=lambda: environ.get('VERB', ''))

    def to_dict(self):
        return asdict(self)

    def update_from_dict(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
