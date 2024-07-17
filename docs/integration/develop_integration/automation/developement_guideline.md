# Development Guidelines

## Tips

### Account Configuration vs. Trigger or Module Configuration

In the context of our development, it's essential to distinguish between account configuration and trigger/module configuration:

- Properties in the configuration field of the `manifest.json` file are related to the account configuration section of the module within the interface.

- Properties found in files like `trigger_(...).json` are associated with trigger configuration, and `action_(...).json` are associated to the configuration of the module.

## Must-Do

### Versioning

When working on an existing module, adhere to the following versioning practice:

- Increment the version number within the `manifest.json` file, follow the Semantic Versioning guidelines available at [Semantic Versioning Specification](https://semver.org/spec/v2.0.0.html).

