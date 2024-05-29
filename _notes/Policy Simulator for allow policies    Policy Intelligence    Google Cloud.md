---
source: cloud.google.com
url: https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview
---

Policy Simulator for Identity and Access Management allow policies lets you see how a change to an allow policy might impact a principal's access before you commit to making the change. You can use Policy Simulator to ensure that the changes you're making won't cause a principal to lose access that they need.

## How Policy Simulator works

Policy Simulator helps you determine what impact a change to an allow policy might have for your users. To do this, it doesn't just compare the permissions in the current and proposed allow policies. Instead, it uses access logs to focus on the permission changes that would actually affect your users.

To find out how a change to an allow policy might impact a principal's access, Policy Simulator determines which access attempts from the last 90 days have different results under the proposed allow policy and the current allow policy. Then, it reports these results as a list of access changes.

When you simulate a change to an allow policy, you provide a proposed allow policy with the changes that you want to test. This proposed allow policy can be for any [resource that accepts allow policies](https://cloud.google.com/iam/docs/resource-types-with-policies).

When you run a simulation, Policy Simulator does the following:

1.  Retrieves access logs for [supported resource types](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#support-levels) from the last 90 days. Where these logs are collected from depends on the resource whose allow policy you're simulating:
    
    -   If you are simulating an allow policy for a project or organization, Policy Simulator retrieves the access logs for that project or organization.
    -   If you are simulating an allow policy for a different type of resource, Policy Simulator retrieves the access logs for that resource's parent project or organization.
    -   If you are simulating multiple resources' allow policies at once, Policy Simulator retrieves the access logs for the resources' nearest common project or organization.
    
    If the parent resource has not existed for 90 days, Policy Simulator retrieves all access attempts since the resource was created.
    
2.  Re-evaluates, or _replays_, the access attempts recorded in the access logs using the current allow policies, taking into account any [inherited allow policies](https://cloud.google.com/iam/docs/policies#inheritance) and any allow policies set on descendant resources.
    
    Replaying access attempts with the current allow policy ensures that Policy Simulator only reports access changes that are a result of the proposed allow policy, and does not report changes that are the result of other allow policy modifications that you've made in the last 90 days.
    
3.  Replays the access attempts again using the proposed allow policy, once more taking into account any inherited allow policies and any allow policies set on descendant resources.
    
4.  Compares the results from the two replays and reports the differences, which show how the proposed changes would affect the principal's access.
    

### Example: Testing policy changes

Imagine that you want to remove a user's Organization Viewer role (`roles/resourcemanager.organizationViewer`). You want to use Policy Simulator to confirm that this change won't affect the user's access.

You use the Google Cloud console, REST API, or the Google Cloud CLI to [simulate the change to the allow policy](https://cloud.google.com/policy-intelligence/docs/simulate-iam-policies).

When you begin the simulation, Policy Simulator does the following:

-   Retrieves the access logs for your organization from the last 90 days.
-   Replays the access attempts using the organization's current allow policy, where the user has the Organization Viewer role.
-   Replays the access attempts again using the proposed allow policy, where the user doesn't have the Organization Viewer role.
-   Compares the results from the two replays and reports the differences between them.

You can then review the results to understand how the proposed change affects the user's access.

### Example: Policy inheritance

Imagine that you want to simulate a change to an allow policy for a folder, `Engineering`, in an organization with the following structure:

![[0916a7d21d192f69c74ab3f88414bb7d_MD5.svg]]

Note that `Engineering` has a parent resource, the organization `example.com`, that it inherits allow policies from. It also has three child projects that can have their own allow policies: `example-prod`, `example-dev`, and `example-test`.

You provide a proposed allow policy and run the simulation. When you begin the simulation, Policy Simulator does the following:

-   Retrieves all relevant logs for the last 90 days. Because `Engineering` is a folder, Policy Simulator retrieves logs from its parent organization, `example.com`.
-   Replays the access attempts using the folder's current allow policy, the allow policy inherited from `example.com`, and the allow policies of the child projects.
-   Replays each access attempt again using the proposed allow policy, the allow policy inherited from `example.com`, and the allow policies of the child projects.
-   Compares the results from the replays and reports the differences between them.

You can then review the results to understand how the proposed change affects the user's access.

## Reviewing Policy Simulator results

Policy Simulator reports the impact of a proposed change to an allow policy as a list of _access changes_. An access change represents an access attempt from the last 90 days that would have a different outcome under the proposed allow policy than under the current allow policy.

Policy Simulator also lists any errors that occurred during the simulation, which helps you identify potential gaps in the simulation.

There are several different types of access changes:

| Access change | Details |
| --- | --- |
| **Access revoked** | The principal had access under the current allow policy, but will no longer have access after the proposed change. |
| **Access potentially revoked** | 
This result can occur for the following reasons:

-   The principal had access under the current allow policy, but their access under the proposed allow policy is [unknown](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#unknown).
-   The principal's access under the current allow policy is [unknown](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#unknown), but they will not have access after the proposed change.

 |
| **Access gained** | The principal did not have access under the current allow policy, but will have access after the proposed change. |
| **Access potentially gained** | 

This result can occur for the following reasons:

-   The principal did not have access under the current allow policy, but their access after the proposed change is [unknown](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#unknown).
-   The principal's access under the current allow policy is [unknown](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#unknown), but they will have access after the proposed change.

 |
| **Access unknown** | The principal's access under both the current allow policy and proposed allow policy is [unknown](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#unknown), and the proposed changes might affect the principal's access. |
| **Error** | An error occurred during the simulation. |

### Unknown results

If an access result is _unknown_, it means that Policy Simulator did not have enough information to fully evaluate the access attempt.

There are several reasons that a result can be unknown:

-   **Role info denied**: The principal running the simulation did not have permission to see the role details for one or more of the roles being simulated.
-   **Unable to access policy**: The principal running the simulation did not have permission to get the allow policy for one or more of the resources involved in the simulation.
-   **Membership info denied**: The principal running the simulation did not have permission to view the members of one or more of the groups included in the simulated allow policy.
-   **Unsupported condition**: There is a conditional role binding in the allow policy that is being tested. Policy Simulator does not support conditions, so the binding could not be evaluated.

If an access result is unknown, the Policy Simulator results report the reason it was unknown, plus the specific roles, allow policies, membership info, and conditionals it was unable to access or evaluate.

### Errors

Policy Simulator also reports any errors that occurred during the simulation. It's important to review these errors so that you understand the potential gaps in the simulation.

There are several types of errors that Policy Simulator might report:

-   **Operation errors**: The simulation could not be run.
    
    If the error message states the simulation could not be run because there are [too many logs](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#max-log-size) in your project or organization, then you cannot run a simulation on the resource.
    
    If you get this error for another reason, try running the simulation again. If you still cannot run the simulation, contact policy-simulator-feedback@google.com.
    
-   **Replay errors**: A replay of a single access attempt was unsuccessful, so Policy Simulator could not determine if the result of the access attempt would change under the proposed allow policy.
    
-   **Unsupported resource type errors**: The proposed allow policy affects permissions associated with an [unsupported resource type](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#support-levels), which Policy Simulator cannot simulate. Policy Simulator lists these permissions in the simulation results so that you know which permissions it was unable to simulate.
    

## Maximum log replay size

The maximum number of access logs that a simulation can replay is 5,000. If there are more than 5,000 access logs for your project or organization for the past 90 days, the simulation will fail.

To learn how Policy Simulator decides which access logs to retrieve, see [How the Policy Simulator works](https://cloud.google.com/policy-intelligence/docs/iam-simulator-overview#how-simulator-works) on this page.

## Support levels for resource types

Policy Simulator does not support all resource types in simulations. This affects the permission changes that it is able to simulate.

### Supported resource types

Policy Simulator supports **only** the following resource types:

| Service | Supported resource types |
| --- | --- |
| Cloud Storage | 
-   `buckets`

 |
| Pub/Sub | 

-   `snapshots`
-   `subscriptions`
-   `topics`

 |
| Cloud SQL | 

-   `backupRuns`
-   `databases`
-   `instances`
-   `sslCerts`
-   `users`

 |
| Spanner | 

-   `backups`
-   `backupOperations`
-   `databases`
-   `databaseOperations`
-   `instanceConfigs`
-   `instanceOperations`
-   `instances`
-   `sessions`

 |
| Resource Manager | 

-   `folders`
-   `organizations`
-   `projects`

 |
| Compute Engine | 

-   `instances`

 |

### Unsupported resource types

Unsupported resource types are resource types that Policy Simulator cannot retrieve access logs for. If Policy Simulator cannot retrieve access logs for a resource, it cannot evaluate how the proposed allow policy could affect those access attempts.

If a proposed change to an allow policy involves permissions for an unsupported resource type, Policy Simulator lists those permissions in the simulation results so that you know which permissions it was unable to simulate. For example, Policy Simulator does not support AI Platform models. So, if a proposed allow policy removes a role with the `aiplatform.models.list` permission, the results for that simulation state that it was unable to simulate the `aiplatform.models.list` permission.

## What's next

-   Learn how to [simulate a change to an allow policy](https://cloud.google.com/policy-intelligence/docs/simulate-iam-policies).
-   Explore other [Policy Intelligence tools](https://cloud.google.com/policy-intelligence/docs/overview).
