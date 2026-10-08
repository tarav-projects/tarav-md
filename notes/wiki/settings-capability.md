# Settings capability

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

Companion to [Capabilities by subtyping](capabilities-by-subtyping.md).

## Motivation

A type may come to extend many capability classes. That is good, because the type then states its capabilities explicitly, but each capability's controls could be custom, and configuring such an object would become a mess. The User proposed one shared place for them, comparable to the long dotted keys of Visual Studio Code settings: a namespace for configuring things. If every extension class looks there for how its capability is controlled, Tarav becomes a more predictable code base and more extensible for the people who build on it.
<!-- tarav.breadcrumb 5e62db511d0202655b7f01a2fdcac27b71058a7283d44e0f0cd4ddc232253a62 -->

## Settings is a capability

Not every object has `.settings`. Settings is another capability. A class that needs controls provides the namespace of its own capability, such as checks, and also declares a settings space, so it hooks into two capabilities at once. An object that extends nothing needing settings has no `.settings` at all.
<!-- tarav.breadcrumb d172619caa0dbe06d6a15ccbc740eed70577f1d9a79c2228da5c9d1311bec3de -->

A capability can also have no settings and be used only by extending its methods. The settings space is offered as the Tarav way to do it when a capability does need configuration.
<!-- tarav.breadcrumb 615e045b464427edfa7559555c0d517962c3384b1677713dd8ef69bc7ee5556f -->

## Declared keys and partitions

Each type that uses settings expresses a template of its expected keys, in the spirit of the record system, and the type controls it. The rules are kept as simple as possible so they are easy to understand: every type has its own partition in the settings, and a type that wants its parent's settings includes them explicitly, as a type includes its parent's checks. The system is type-internal; it was not conceived as a route to project settings.
<!-- tarav.breadcrumb 32f221ad020976da93091665f73faa443e093f42bdebd8d04e98aeae6f93a12f -->

## Entry points

There are two standard entry points. A settings object can be passed at construction, and the settings namespace offers a write operation to set or update values on an existing object. Both are conventions. A type may do it differently, and a wrong choice can be fixed later. Using the standard path gives the checks for free, such as a key the type does not declare, and connects the settings to the object's context so they can be navigated.
<!-- tarav.breadcrumb fdeff8e1079a0ba4fb80eb67588e7cdd3c555262bba7031953bafde297528029 -->

## What is not regulated

The system only says where settings live. How a setting operates and how it is used are open. When a workflow reads a number from the settings, what it does with it is an implementation detail. Locking is therefore not a settings feature: a tracking workflow that wants an always-tracked type reads its setting and does one thing or another.
<!-- tarav.breadcrumb 876228071d7cffacc5a6e4ba2b543836f4f4e7e1940d9ad2d0541f346d803de7 -->

## Sources of values

Object settings and files are the same workflow. Settings may be loaded from a file when a type wants that, and how defaults are created and how settings are loaded stays flexible. The system fixes semantic places, not how they are connected. It can become a general way to handle settings, at runtime or connected to files, and Tarav's own settings machinery might use it.
<!-- tarav.breadcrumb ec386b99fbe1af80df7f3ebfd34cbda28289fbe9ccf38b10c132fee272b8ef8a -->

## Settings are not object data

Settings are for configuration. Trying to hold object data in them is one of the typical failure points.
<!-- tarav.breadcrumb 09383fe22beefcf22e5e5e15d2f42d2a26c9f7a6445a12af47558ee45b4998f8 -->

The split is tricky but important. Loading a record does not put its data into `.settings`. A class can represent settings: that content is then its data, held in proper fields. The same class can itself have `.settings`, and those configure how the class behaves, because a type and its functionality have a configuration space of their own that needs to be modeled.
<!-- tarav.breadcrumb a02dc18e2d53d671a9674350d7b02a79f9eff41004aeba70caa682e7f5b09d39 -->

## Agent proposals, not decided

These points came from the agent during the discussion. The User has not confirmed them.

- Recording where each value came from (type default, construction, runtime change or file), so behaviour stays explainable once several sources exist.
- Starting with two levels only, the class default and the instance.
- Classifying the `agents` entry added to the Project marker on 2026-10-08: the main file name and the aliases would be data, and the two switches that turn the system prompt checks off would be settings that happen to be stored in the marker.

One agent claim was retracted after the User's correction: that Tarav's configuration files would become settings templates. Those files are the data of objects that represent configuration, and declaring and validating their fields is the record system's job.
