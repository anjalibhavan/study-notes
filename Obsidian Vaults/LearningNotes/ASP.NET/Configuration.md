
Iconfiguration passed to Startup class via dependency injection can be used to set configurations for app.

The ASPNETCORE_ENVIRONMENT variable in launchsettings is used to set the env of the application. We can add an extension configureappconfiguration function to the createdefaultbuilder in program.cs that looks for appsettings.json and appsettings.envname.json files and reads config values from them, and adds them as config sources to the app along with other sources like command line.

Config sources take precedence based on the order in which they are added to the app.

If we want these values to be available to service and controller we can dependency inject them.

We don't want sensitive info in appsettings during dev so we can use secret manager for that. dotnet user-secrets init initializes a secret manager.

To set a value: dotnet user-secrets set "MyApi:MyApiKey", "Sensitive data!".

Can be managed from IDE in VS.