osint-lab/
├── .devcontainer/ # devcontainer (Dockerfile + devcontainer.json)
│ └── Dockerfile
│ └── devcontainer.json
├── .vscode/ # optional VS Code settings / launch configs
│ └── settings.json
├── attacker/ # attacker tooling & scripts (all lab-only)
│ ├── **init**.py
│ ├── example_enum.py # small starter enumerator (curl/requests)
│ ├── enumerate_lab.py # the runner you used to snapshot site -> reports/
│ ├── normalize_reports.py # parses report folders -> all_findings.json/.csv
│ ├── requirements.txt # python libs for scripts
│ └── README.md # how to run attacker scripts
├── target/ # local test target files (if not using GitHub Pages)
│ ├── index.html
│ ├── team.html
│ └── robots.txt
├── reports/ # auto-created by scripts; keep scan outputs here
│ └── README.md # explain naming convention & sensitive-data policy
│ # e.g. reports/yourlab.com-20250929T...Z/ -> robots.txt, headers.txt, etc.
├── docs/ # optional: reports, slides, writeups
│ └── findings.md # your human-friendly summary report
├── .gitignore
├── Makefile # convenience targets (venv, install, run)
├── README.md # project overview + resume-friendly blurb
└── LICENSE # optional
