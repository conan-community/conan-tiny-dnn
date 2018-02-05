from conan.packager import ConanMultiPackager
import os, re, platform


def get_value_from_recipe(search_string):
    with open("conanfile.py", "r") as conanfile:
        contents = conanfile.read()
        result = re.search(search_string, contents)
    return result

def get_name_from_recipe():
    return get_value_from_recipe(r'''name\s*=\s*["'](\S*)["']''').groups()[0]

def get_version_from_recipe():
    return get_value_from_recipe(r'''version\s*=\s*["'](\S*)["']''').groups()[0]

def get_default_vars():
    username = os.getenv("CONAN_USERNAME", "conan")
    channel = os.getenv("CONAN_CHANNEL", "stable")
    version = get_version_from_recipe()
    return username, channel, version

def is_ci_running():
    return os.getenv("APPVEYOR_REPO_NAME","") or os.getenv("TRAVIS_REPO_SLUG","")

def get_ci_vars():
    reponame_a = os.getenv("APPVEYOR_REPO_NAME","")
    repobranch_a = os.getenv("APPVEYOR_REPO_BRANCH","")

    reponame_t = os.getenv("TRAVIS_REPO_SLUG","")
    repobranch_t = os.getenv("TRAVIS_BRANCH","")

    username, _ = reponame_a.split("/") if reponame_a else reponame_t.split("/")
    channel, version = repobranch_a.split("/") if repobranch_a else repobranch_t.split("/")
    return username, channel, version

def get_env_vars():
    return get_ci_vars() if is_ci_running() else get_default_vars()

def get_os():
    return platform.system().replace("Darwin", "Macos")

if __name__ == "__main__":
    name = get_name_from_recipe()
    username, channel, version = get_default_vars()
    login_username = os.getenv("CONAN_LOGIN_USERNAME", "conanbot")
    reference = "{0}/{1}".format(name, version)
    upload_remote = "https://api.bintray.com/conan/conan-community/{0}".format(username)

    builder = ConanMultiPackager(
        username=username,
        channel=channel,
        login_username=login_username,
        reference=reference,
        upload=upload_remote,
        remotes=upload_remote)

    builder.add_common_builds()

    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if settings["compiler"] == "gcc":
            filtered_builds.append([settings, options, env_vars, build_requires])
            break

    builder.builds = filtered_builds
    builder.run()
