**PLEASE READ**: If you have a support contract with Google, please create an issue in the [support console](https://cloud.google.com/support/) instead of filing it on GitHub. This will ensure a timely response.

To help us resolve your issue as soon as possible, please follow these steps:


<a id="org49b5b6e"></a>

# Check for already opened issues:

-   In `google-cloud-python`: <https://github.com/googleapis/google-cloud-python/issues>


<a id="orge74b7aa"></a>

# *BEFORE* reporting an issue here

-   Please determine whether it's a client library issue or an underlying API service issue.
    -   **Bugs**: Try reproducing the issue without the client library; if you can, then it's an API issue.
    -   **Features**: Determine whether you want something different about the data or how it's changed in Google services (rather than how you access or manipulate it locally); if so, it's an API issue.
-   To make these determinations, visit [Google APIs Explorer](https://developers.google.com/apis-explorer):
    1.  Find your API on the [APIs Explorer list](https://developers.google.com/apis-explorer), and follow the link.
    2.  Click on the API method corresponding to your issue.
    3.  In the page that appears:
        -   You can use the APIs Explorer sidebar (“Try this Method”), fill in your request parameters, and see whether your request succeeds or causes the same error you were getting initially.
        -   Alternatively, you can use the `HTTP Request` listed on that page and any information on the `Request body` to construct a request you can send from the command line using a tool like `curl`.
    4.  If your request in step 3 above succeeds and is as you expect, then it's likely the resolution centers on the client library; [file a client library issue](#orge13c134) as detailed below. If your request failed or returned unexpected results, then it's likely the resolution centers on the API service; [file an API service issue](#orgb8af98c) instead, as detailed below.


<a id="orgb8af98c"></a>

# Filing an API service issue

*(if the issue DID re-occur [above](#orge74b7aa) without using the client library)*

Use the appropriate API service issue tracker. The maintainers of this repo are not experts or contributors on individual API services; we work on generating usable and idiomatic client libraries for many APIs.

1.  Consider using [Google Cloud Customer Care](https://cloud.google.com/support/?hl=en) (paid) to get more dedicated support for your issue. Otherwise, continue with the steps below.
2.  Find your API in [the client list at the top of this repository](https://github.com/googleapis/google-cloud-python/tree/main?tab=readme-ov-file#libraries).
3.  Check the “API Issues” column to see whether someone else has reported the same issue. If they have, the filed issue may have some useful information; feel free to add more details or context of your own.
4.  If your issue has not been filed, you can click on “File an API Issue” from the same [client list](https://github.com/googleapis/google-cloud-python/tree/main?tab=readme-ov-file#libraries) to notify the API service team. Be as complete yet succinct as you can!
5.  If you don't see the "API Issues" column for this API (we're in the process of filling out the table), go ahead and file an issue in this repository and make a note that it's likely a service-side issue.  We will route it to the right service team.


<a id="orge13c134"></a>

# Filing a client library issue

*(if the issue DID NOT re-occur [above](#orge74b7aa) without using the client library)*

Consider using [Google Cloud Customer Care](https://cloud.google.com/support/?hl=en) (paid) to get more dedicated support for your issue. Otherwise, continue with the steps below.

-   Determine the right repository in which to file:
    -   If you fetched the API-specific PyPI package, you are probably using one of the modern Python [Cloud Client Libraries](https://cloud.google.com/apis/docs/cloud-client-libraries). Go to  [the client list at the top of this repository](https://github.com/googleapis/google-cloud-python/tree/main?tab=readme-ov-file#libraries), which lists them all, and click on the name of your client. That will take you to the correct repository in which to file an issue (for the many APIs listed under [`packages/`](https://github.com/googleapis/google-cloud-python/tree/main/packages), it's this repo, `google-cloud-python`).
    -   If you're using the package `googleapiclient` in your code, you are using the older Python [Google API Client Libraries](https://developers.google.com/api-client-library/), whose source code is hosted in the repository [google-api-python-client](https://github.com/googleapis/google-api-python-client); please file an issue there for those.
    -   For more information on the difference between Cloud Client Libraries and Google API Client Libraries, see [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).
-   Go to the correct repository, as identified above
    1.  Search for issues already opened (in this repository, those would be in <https://github.com/googleapis/google-cloud-python/issues>). If you find your problem already filed, just add any more context or details that seem appropriate.
    2.  If your problem has not been previously filed, file an issue. If you're filing  in this repository, choose either the [bug report](https://github.com/googleapis/google-cloud-python/issues/new?template=bug_report.yaml) or [feature request](https://github.com/googleapis/google-cloud-python/issues/new?template=feature_request.yaml) template, fill in the details, and submit the issue with an informative title!

