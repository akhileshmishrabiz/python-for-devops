from google.cloud import resourcemanager_v3

def get_folders(
    parent_id = "organizations/ORGANIZATION_ID",
    folders = None):

# This function will return a list of folder_id for all the folders and 
# subfolders respectively

    if folders is None:
        folders = []

# Creating folder client 
    client = resourcemanager_v3.FoldersClient()
    request = resourcemanager_v3.ListFoldersRequest(
        parent=parent_id,
    )

    page_result = client.list_folders(request=request)
    for pages in page_result:
        folders.append(pages.name)
        get_folders(parent_id=pages.name, folders=folders)
    return folders


def search_projects(folder_id):
# This function will take folder_id input and returns
# the list of project_id under a given folder_id

    client = resourcemanager_v3.ProjectsClient()

    query = f"parent:{folder_id}"
    request = resourcemanager_v3.SearchProjectsRequest(query=query)
    page_result = client.search_projects(request=request)
    search_result = []
    for pages in page_result:
        search_result.append(pages)
    return search_result


def list_projects():
# will returns the list of all active projects(project_id)

    active_project = []
    for folders in get_folders(parent_id="organizations/ORGANIZATION_ID", folders=None):
        for projects in search_projects(folders):
            if str(projects.state) == "State.ACTIVE":
                active_project.append(projects.project_id)

    return active_project


if __name__ == "__main__":
    print(list_projects())
