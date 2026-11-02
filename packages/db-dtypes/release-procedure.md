# db-dtypes release procedure

*   Checkout main branch

        git fetch upstream main
        git checkout main
        git rebase -i upstream/main

*   Update version number in `setup.py`

*   Update `CHANGELOG.md`

*   Commit and push

        git commit -m "Release x.x.x"
        git push upstream main

*   Build the package

        git clean -xfd
        python setup.py register sdist bdist_wheel --universal

*   Upload to test PyPI

        twine upload --repository testpypi dist/*

*   Try out test PyPI package

        pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple db-dtypes

*   Upload to PyPI

        twine upload dist/*

*   Tag release on GitHub
