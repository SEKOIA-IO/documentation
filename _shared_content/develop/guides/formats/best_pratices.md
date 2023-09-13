# Best Pratices

Raw events may represent information in different ways. For each datasource, the parser will extract important information and generate a normalized JSON document.

This document describes some principles can help define how to generate the JSON document.

## A user authenticate on a Windows Host

This event, from a Windows host, describes a successfully authentication:

```

```

For this event, the parser will follow these principles:

- Set **event**.category to the category `authentication`
- Set **event**.category to `start`
- Set **action**.outcome to `success`
- Set **user*.name with the name of the principal
