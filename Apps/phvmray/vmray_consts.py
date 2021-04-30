VMRAY_JSON_SERVER = "vmray_server"
VMRAY_JSON_API_KEY = "vmray_api_key"
VMRAY_JSON_DISABLE_CERT = "disable_cert_verification"
VMRAY_ERR_SERVER_CONNECTION = "Could not connect to server"
VMRAY_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
VMRAY_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
VMRAY_ERR_UNSUPPORTED_HASH = "Unsupported hash"
VMRAY_ERR_SAMPLE_NOT_FOUND = "Could not find sample"
VMRAY_ERR_OPEN_ZIP = "Could not open zip file"
VMRAY_ERR_ADD_VAULT = "Could not add file to vault"
VMRAY_ERR_MULTIPART = ("File is a multipart sample. Multipart samples are "
                       "not supported")
VMRAY_ERR_MALFORMED_ZIP = "Malformed zip"
VMRAY_ERR_SUBMIT_FILE = "Could not submit file"
VMRAY_ERR_GET_SUBMISSION = "Could not get submission"
VMRAY_ERR_SUBMISSION_NOT_FINISHED = "Submission is not finished"
VMRAY_ERR_NO_SUBMISSIONS = "Sample has no submissions"
VMRAY_ERR_FILE_EXISTS = "File already exists"

ACTION_ID_VMRAY_GET_FILE = "get_file"
ACTION_ID_VMRAY_DETONATE_FILE = "detonate_file"
ACTION_ID_VMRAY_DETONATE_URL = "detonate_url"
ACTION_ID_VMRAY_GET_REPORT = "get_report"
ACTION_ID_VMRAY_GET_INFO = "get_info"

VMRAY_DEFAULT_PASSWORD = b"infected"
VAULT_TMP_FOLDER = "/vault/tmp"
DEFAULT_TIMEOUT = 60 * 10

VMRAY_SEVERITY_NOT_SUSPICIOUS = "not_suspicious"
VMRAY_SEVERITY_SUSPICIOUS = "suspicious"
VMRAY_SEVERITY_MALICIOUS = "malicious"
VMRAY_SEVERITY_BLACKLISTED = "blacklisted"
VMRAY_SEVERITY_WHITELISTED = "whitelisted"
VMRAY_SEVERITY_UNKNOWN = "unknown"
VMRAY_SEVERITY_ERROR = "error"
