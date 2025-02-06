<<<<<<< HEAD
# orbitcabs
=======
### Orbit Cabs

Quick and affordable cabs right at your doorsteps.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch main
bench install-app orbitcabs
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ez8F0nW6S-w?si=ZCY_lyVq577_2xWV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[![Watch the video](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)


[![Watch the video](https://youtu.be/Ez8F0nW6S-w?si=AtZCNqDuB4H8fth4)

<video width="600" controls>
  <source src="[https://github.com/user/repo/assets/123456/demo.mp4](https://youtu.be/Ez8F0nW6S-w?si=AtZCNqDuB4H8fth4)" type="video/mp4">
  Your browser does not support the video tag.
</video>



### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/orbitcabs
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
>>>>>>> 76924d2 (feat: Initialize App)
