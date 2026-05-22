# Add custom instructions for Elevate agents

If you want to refined the agent investigation results you can add custom instructions. 

## Add Contextual instructions
If you want add more context for a specific community: 
1. Go to **Settings > AI agent**.
2. Select the community where you want the change to be applied.
3. Select **Agent/Alert case investigation**.
4. Open the **Instructions** tab.
5. Enter your custom instructions.
6. Select **Save**.

!!! note "Workspace instructions"
   If you want this instruction to be applied on all your communities, Select your workspace instead of a specific community.

## Custom detection rules agent investigation

!!! tip
   - If the triggering rules comes from a runbook you have created, you can modify the Reasoning questions sections that the agent will use. 
   - If the triggering rules comes from a runbook build by Sekoia, you can duplicate the rule and edit the runbook but this duplicated rules won't be automatically updated by Sekoia.

   1. If you want to change the reasoning questions, in the Triggered rule section, click on the **Runbook** button.
   2. At the bottom of the runbook panel, click on **Edit Runbook**.
   3. Modify the reasoning questions according to your preferences.
   4. Click **Save runbook**.
As soon as an alert is triggered by this detection rule the agent takes your modification into account.

!!! note "Communities impacted"
    These modifications apply to all the communities from your workspace.
   
