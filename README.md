# ExportCommentsAPI
***A unofficial Python client for the ExportComments API.***

💡 This repositry is an easy-to-use tool to export social media comments massively and safely.


| # | Official Client | Our Client |
| --- | --- | --- |
| A | N/A | Yes |
| B | N/A | Yes |

>**Note**: **ExportComments is a paid service!**
> You need to create a [BUSINESS access](https://exportcomments.com/pricing) account to use the service.


# 1. Install *`ExportComments`*:
  **One-Step Automated Install:**
  
  Those who want to get started quickly and conveniently may install ExportComments API endpoints using `requirements.txt`

  **Alternative Install Methods:**
  - You can use pip to install the library:
    ```bash
    $ pip install exportcomments
    ```

- Or, you can just clone [the official python client repository](https://github.com/exportcomments/exportcomments-python) and run the setup.py script:

  ```bash
  $ python setup.py install
  ```

## 2. Next? Clone our repository and run

To specify a specific folder to clone to, add the name of the folder after the repository URL, like this: 
```bash
$ git clone https://github.com/0xMakrem/ExportCommentsAPI.git myfolder
```
Manualy edit your configuration file `config.json` with the correct informations:
| # | Description |
| --- | --- |
| `log` | Log file |
| `input` | URL input file name |
| `output` | Comments output file name |
| `token` | ExportComments API Access Token |

Alternatively, you can manually edit configuration information in code directly.

🚸 Please edit the file carefully
```python
log="log.xlsx" #Log file
input_="filename.xlsx" #Input file
output_="filename.xlsx" #Output file
token="############" #ExportComments API Access Token
```
<!-- ROADMAP -->
## Roadmap

- [x] Add *Facebook comments exportation* :tada:
- [x] Add *Merge collected comments in one file* :tada:
- [x] Add *Remove all personal information* :tada:
- [ ] Add Errors and Exceptions log


See the [open issues](https://github.com/0xMakrem/ExportCommentsAPI/issues) for a full list of proposed features (and known issues).
