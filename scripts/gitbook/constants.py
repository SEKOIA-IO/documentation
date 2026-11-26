BULK_SIZE = 500
API_URL = "https://api.gitbook.com/v1"
PREFIXES = {
    "intake": "/operation_center/integration_catalog/uuid/",
    "playbook": "/integration/action_library/uuid/",
    "asset": "/integration/asset_connectors/uuid/",
}

# HTTP settings
TIMEOUT = 30  # seconds
RETRIES = 3
RETRY_STATUSES = (429, 500, 502, 503, 504)
ERROR_TEXT_LENGTH = 500  # characters of the response body kept in error messages

# safety guards: above these shares, --apply is refused unless --force is given
MAX_MISSING_PAGES_RATIO = 0.2  # share of uuids whose file has no GitBook page
MAX_DELETE_RATIO = 0.2  # share of the managed redirects to delete
