# Massive export of events

The following script can be used to trigger massive exports of events.

```python
"""
Sekoia.io Export Script

This script exports search job results from Sekoia.io API.
Usage: python export.py <job_uuid>
"""

import os
import sys
import time
from datetime import datetime

import requests
import argparse

API_HOST = "api.sekoia.io"

def create_http_session() -> requests.Session:
    # Load API key from environment variable
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.")
        return

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {api_key}"
    })

    return session

def export(job_uuid: str) -> None:
    """Export search job results and poll for completion.
    
    Args:
        job_uuid: The UUID of the search job to export
    """

    session = create_http_session()

    # Trigger the export
    response = session.post(
        f"https://{API_HOST}/v1/sic/conf/events/search/jobs/{job_uuid}/export"
    )
    if response.status_code != 200:
        print(f"Failed to trigger export: {response.status_code} {response.text}")
        return

    task_uuid = response.json().get("task_uuid")
    if not task_uuid:
        print("No task UUID returned from export trigger.")
        return
    
    print(f"Export task triggered with UUID: {task_uuid}")

    status(task_uuid, session)

def status(task_uuid: str, session: requests.Session | None = None) -> None:
    """Check the status of an export task."""

    if session is None:
        session = create_http_session()

    # Poll for export completion
    is_ready = False
    start_time = datetime.now()
    
    while not is_ready:
        time.sleep(2)  # Wait before polling

        response = session.get(f"https://{API_HOST}/v1/tasks/{task_uuid}")
        if response.status_code != 200:
            print(f"Failed to get export status: {response.status_code} {response.text}")
            return

        data = response.json()
        is_ready = data.get("status") == "FINISHED"
        status = data.get("status")
        if is_ready:
            download_url = data.get("attributes", {}).get("download_url")
            if download_url:
                print(f"Export ready! Download URL: {download_url}")
            else:
                print("Export finished but no download URL found.")
        else:
            total = data.get('total', 0)
            progress_count = data.get('progress', 0)
            
            if total > 0:
                progress = 100 * progress_count / total
                
                # Calculate estimated time of completion
                elapsed = datetime.now() - start_time
                if progress_count > 0:
                    estimated_total_time = elapsed * (total / progress_count)
                    eta = start_time + estimated_total_time
                    eta_str = eta.strftime('%H:%M:%S')
                else:
                    eta_str = f"calculating... ({status})"

                current_time = datetime.now().strftime('%H:%M:%S')
                print(f"{current_time} {progress:.2f}% ({progress_count}/{total}) "
                      f"completed... ETA: {eta_str}")


def main() -> None:
    """Main function to handle command line arguments and run export."""
    parser = argparse.ArgumentParser(description='Sekoia.io Export Script')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export search job results')
    export_parser.add_argument('job_uuid', help='The UUID of the search job to export')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Check export job status')
    status_parser.add_argument('task_uuid', help='The UUID of the export task')
    
    args = parser.parse_args()
    
    if args.command == 'export':
        export(args.job_uuid)
    elif args.command == 'status':
        status(args.task_uuid)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
```
