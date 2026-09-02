# Refactored Pyterprise — Object-Oriented Terraform Cloud/Enterprise API Client

A highly modified, expanded, and production-hardened fork of the original `pyterprise` library, optimized to orchestrate mass workspace automation pipelines within large-scale multi-region cloud infrastructures.

## 🚀 Background & Attribution
This repository is an extensive refactor built upon the base logic of the open-source [pyterprise package found on PyPI](https://pypi.org/project/pyterprise/ ). Due to legacy constraints and deprecations in the original upstream code, this version was completely overhauled to support modern Terraform Cloud / Enterprise REST API endpoints, enterprise-grade authentication, and dynamic workspace synchronization state patterns.

---

## 🛠️ Key Architectural Enhancements
*   **Modern API Mapping:** Updated core methods to align with current HashiCorp Terraform Enterprise schemas.
*   **Bulk Execution Capabilities:** Enhanced payload management to safely trigger, confirm, or discard workspace runs across hundreds of environments programmatically without hitting API rate limits.
*   **Strict Error Trapping:** Implemented advanced exception handling for remote state distributions, credential updates, and OAuth VCS token connection flows.

---

## ⚙️ Usage Reference

```python
import pyterprise

# Instantiate the modernized enterprise client
client = pyterprise.Client()
client.init(
    token="YOUR_SECURE_TFE_TOKEN", 
    url="https: /  / ://company.com"
)

# Target isolated organization scope
org = client.set_organization(id="enterprise-org-name")

# Programmatically track and orchestrate workspace configurations
for workspace in org.list_workspaces():
    print(f"Tracking: {workspace.name} [{workspace.id}]")
    
    # Inject workspace environment variables safely
    workspace.create_variable(
        key="CONF_ENV", 
        value="production", 
        sensitive=False, 
        category="env"
    )
```

---
*🤖 Automated by code, refactored and maintained with ❤️ by **elserhumano**.*
