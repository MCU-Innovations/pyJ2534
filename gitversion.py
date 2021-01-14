import git


def get_version():
    r = git.repo.Repo(search_parent_directories=True)
    version = r.git.describe("--tags")[1:]
    if "-" in version:
        version = ".".join(version.split("-")[:-1])
    return version


__VERSION__ = get_version()

if __name__ == "__main__":
    print(__VERSION__)
