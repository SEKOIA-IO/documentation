declare module 'astro:content' {
	interface Render {
		'.mdx': Promise<{
			Content: import('astro').MarkdownInstance<{}>['Content'];
			headings: import('astro').MarkdownHeading[];
			remarkPluginFrontmatter: Record<string, any>;
		}>;
	}
}

declare module 'astro:content' {
	interface Render {
		'.md': Promise<{
			Content: import('astro').MarkdownInstance<{}>['Content'];
			headings: import('astro').MarkdownHeading[];
			remarkPluginFrontmatter: Record<string, any>;
		}>;
	}
}

declare module 'astro:content' {
	export { z } from 'astro/zod';

	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	// This needs to be in sync with ImageMetadata
	export type ImageFunction = () => import('astro/zod').ZodObject<{
		src: import('astro/zod').ZodString;
		width: import('astro/zod').ZodNumber;
		height: import('astro/zod').ZodNumber;
		format: import('astro/zod').ZodUnion<
			[
				import('astro/zod').ZodLiteral<'png'>,
				import('astro/zod').ZodLiteral<'jpg'>,
				import('astro/zod').ZodLiteral<'jpeg'>,
				import('astro/zod').ZodLiteral<'tiff'>,
				import('astro/zod').ZodLiteral<'webp'>,
				import('astro/zod').ZodLiteral<'gif'>,
				import('astro/zod').ZodLiteral<'svg'>,
				import('astro/zod').ZodLiteral<'avif'>,
			]
		>;
	}>;

	type BaseSchemaWithoutEffects =
		| import('astro/zod').AnyZodObject
		| import('astro/zod').ZodUnion<[BaseSchemaWithoutEffects, ...BaseSchemaWithoutEffects[]]>
		| import('astro/zod').ZodDiscriminatedUnion<string, import('astro/zod').AnyZodObject[]>
		| import('astro/zod').ZodIntersection<BaseSchemaWithoutEffects, BaseSchemaWithoutEffects>;

	type BaseSchema =
		| BaseSchemaWithoutEffects
		| import('astro/zod').ZodEffects<BaseSchemaWithoutEffects>;

	export type SchemaContext = { image: ImageFunction };

	type DataCollectionConfig<S extends BaseSchema> = {
		type: 'data';
		schema?: S | ((context: SchemaContext) => S);
	};

	type ContentCollectionConfig<S extends BaseSchema> = {
		type?: 'content';
		schema?: S | ((context: SchemaContext) => S);
	};

	type CollectionConfig<S> = ContentCollectionConfig<S> | DataCollectionConfig<S>;

	export function defineCollection<S extends BaseSchema>(
		input: CollectionConfig<S>
	): CollectionConfig<S>;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[]
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[]
	): Promise<CollectionEntry<C>[]>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
			  }
			: {
					collection: C;
					id: keyof DataEntryMap[C];
			  }
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"docs": {
"automate/actions.md": {
	id: "automate/actions.md";
  slug: "automate/actions";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/build-playbooks.md": {
	id: "automate/build-playbooks.md";
  slug: "automate/build-playbooks";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/debug-playbooks.md": {
	id: "automate/debug-playbooks.md";
  slug: "automate/debug-playbooks";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/index.md": {
	id: "automate/index.md";
  slug: "automate";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/manage-accounts.md": {
	id: "automate/manage-accounts.md";
  slug: "automate/manage-accounts";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/navigate-playbooks.md": {
	id: "automate/navigate-playbooks.md";
  slug: "automate/navigate-playbooks";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/operators.md": {
	id: "automate/operators.md";
  slug: "automate/operators";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/playbooks-on-premises.md": {
	id: "automate/playbooks-on-premises.md";
  slug: "automate/playbooks-on-premises";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automate/triggers.md": {
	id: "automate/triggers.md";
  slug: "automate/triggers";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automation/create_a_module.md": {
	id: "automation/create_a_module.md";
  slug: "automation/create_a_module";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"automation/overview.md": {
	id: "automation/overview.md";
  slug: "automation/overview";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/enrichers.md": {
	id: "consume/enrichers.md";
  slug: "consume/enrichers";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/export.md": {
	id: "consume/export.md";
  slug: "consume/export";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/feeds.md": {
	id: "consume/feeds.md";
  slug: "consume/feeds";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/graph_explorations.md": {
	id: "consume/graph_explorations.md";
  slug: "consume/graph_explorations";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/intelligence.md": {
	id: "consume/intelligence.md";
  slug: "consume/intelligence";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/ioccollections.md": {
	id: "consume/ioccollections.md";
  slug: "consume/ioccollections";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/observables.md": {
	id: "consume/observables.md";
  slug: "consume/observables";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"consume/telemetry.md": {
	id: "consume/telemetry.md";
  slug: "consume/telemetry";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/create_a_format.md": {
	id: "formats/create_a_format.md";
  slug: "formats/create_a_format";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/datasources.md": {
	id: "formats/datasources.md";
  slug: "formats/datasources";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/overview.md": {
	id: "formats/overview.md";
  slug: "formats/overview";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/parser.md": {
	id: "formats/parser.md";
  slug: "formats/parser";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/smartdescriptions.md": {
	id: "formats/smartdescriptions.md";
  slug: "formats/smartdescriptions";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/structured_event.md": {
	id: "formats/structured_event.md";
  slug: "formats/structured_event";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"formats/taxonomy.md": {
	id: "formats/taxonomy.md";
  slug: "formats/taxonomy";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"guides/authentication_overview.md": {
	id: "guides/authentication_overview.md";
  slug: "guides/authentication_overview";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"guides/filtering.md": {
	id: "guides/filtering.md";
  slug: "guides/filtering";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"guides/get_started.md": {
	id: "guides/get_started.md";
  slug: "guides/get_started";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/anomali.md": {
	id: "integrations/anomali.md";
  slug: "integrations/anomali";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/api.md": {
	id: "integrations/api.md";
  slug: "integrations/api";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/index.md": {
	id: "integrations/index.md";
  slug: "integrations";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/microsoft-sentinel.md": {
	id: "integrations/microsoft-sentinel.md";
  slug: "integrations/microsoft-sentinel";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/misp.md": {
	id: "integrations/misp.md";
  slug: "integrations/misp";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/opencti.md": {
	id: "integrations/opencti.md";
  slug: "integrations/opencti";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/paloalto_xsoar.md": {
	id: "integrations/paloalto_xsoar.md";
  slug: "integrations/paloalto_xsoar";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/splunk.md": {
	id: "integrations/splunk.md";
  slug: "integrations/splunk";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/taxii.md": {
	id: "integrations/taxii.md";
  slug: "integrations/taxii";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"integrations/thehive.md": {
	id: "integrations/thehive.md";
  slug: "integrations/thehive";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/aws.md": {
	id: "library/aws.md";
  slug: "library/aws";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/azure-active-directory.md": {
	id: "library/azure-active-directory.md";
  slug: "library/azure-active-directory";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/binaryedge-s-api.md": {
	id: "library/binaryedge-s-api.md";
  slug: "library/binaryedge-s-api";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/censys.md": {
	id: "library/censys.md";
  slug: "library/censys";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/certificate-transparency.md": {
	id: "library/certificate-transparency.md";
  slug: "library/certificate-transparency";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/crowdstrike-falcon.md": {
	id: "library/crowdstrike-falcon.md";
  slug: "library/crowdstrike-falcon";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/crowdstrike.md": {
	id: "library/crowdstrike.md";
  slug: "library/crowdstrike";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/cybereason.md": {
	id: "library/cybereason.md";
  slug: "library/cybereason";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/darktrace.md": {
	id: "library/darktrace.md";
  slug: "library/darktrace";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/detection-rules.md": {
	id: "library/detection-rules.md";
  slug: "library/detection-rules";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/digital-shadows.md": {
	id: "library/digital-shadows.md";
  slug: "library/digital-shadows";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/duo.md": {
	id: "library/duo.md";
  slug: "library/duo";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/fileutils.md": {
	id: "library/fileutils.md";
  slug: "library/fileutils";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/fortigate-firewalls.md": {
	id: "library/fortigate-firewalls.md";
  slug: "library/fortigate-firewalls";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/fortigate-fw.md": {
	id: "library/fortigate-fw.md";
  slug: "library/fortigate-fw";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/git.md": {
	id: "library/git.md";
  slug: "library/git";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/github.md": {
	id: "library/github.md";
  slug: "library/github";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/glimps.md": {
	id: "library/glimps.md";
  slug: "library/glimps";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/google.md": {
	id: "library/google.md";
  slug: "library/google";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/harfanglab.md": {
	id: "library/harfanglab.md";
  slug: "library/harfanglab";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/http.md": {
	id: "library/http.md";
  slug: "library/http";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/iknowwhatyoudownload.md": {
	id: "library/iknowwhatyoudownload.md";
  slug: "library/iknowwhatyoudownload";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/imperva.md": {
	id: "library/imperva.md";
  slug: "library/imperva";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/iptoasn.md": {
	id: "library/iptoasn.md";
  slug: "library/iptoasn";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/jumpcloud-directory-insights.md": {
	id: "library/jumpcloud-directory-insights.md";
  slug: "library/jumpcloud-directory-insights";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/mandrill.md": {
	id: "library/mandrill.md";
  slug: "library/mandrill";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/mattermost.md": {
	id: "library/mattermost.md";
  slug: "library/mattermost";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/microsoft-azure.md": {
	id: "library/microsoft-azure.md";
  slug: "library/microsoft-azure";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/microsoft-office365.md": {
	id: "library/microsoft-office365.md";
  slug: "library/microsoft-office365";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/misp.md": {
	id: "library/misp.md";
  slug: "library/misp";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/mwdb.md": {
	id: "library/mwdb.md";
  slug: "library/mwdb";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/netskope.md": {
	id: "library/netskope.md";
  slug: "library/netskope";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/okta.md": {
	id: "library/okta.md";
  slug: "library/okta";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/onyphe.md": {
	id: "library/onyphe.md";
  slug: "library/onyphe";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/openai.md": {
	id: "library/openai.md";
  slug: "library/openai";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/osint.md": {
	id: "library/osint.md";
  slug: "library/osint";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/pagerduty.md": {
	id: "library/pagerduty.md";
  slug: "library/pagerduty";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/panda-security.md": {
	id: "library/panda-security.md";
  slug: "library/panda-security";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/proofpoint.md": {
	id: "library/proofpoint.md";
  slug: "library/proofpoint";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/public-suffix.md": {
	id: "library/public-suffix.md";
  slug: "library/public-suffix";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/riskiq.md": {
	id: "library/riskiq.md";
  slug: "library/riskiq";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/rss.md": {
	id: "library/rss.md";
  slug: "library/rss";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/salesforce.md": {
	id: "library/salesforce.md";
  slug: "library/salesforce";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/sekoia-io.md": {
	id: "library/sekoia-io.md";
  slug: "library/sekoia-io";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/sentinelone.md": {
	id: "library/sentinelone.md";
  slug: "library/sentinelone";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/servicenow.md": {
	id: "library/servicenow.md";
  slug: "library/servicenow";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/shodan.md": {
	id: "library/shodan.md";
  slug: "library/shodan";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/skyhigh-security-secure-web-gateway-swg.md": {
	id: "library/skyhigh-security-secure-web-gateway-swg.md";
  slug: "library/skyhigh-security-secure-web-gateway-swg";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/skyhigh-security.md": {
	id: "library/skyhigh-security.md";
  slug: "library/skyhigh-security";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/sophos.md": {
	id: "library/sophos.md";
  slug: "library/sophos";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/stix.md": {
	id: "library/stix.md";
  slug: "library/stix";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/tehtris.md": {
	id: "library/tehtris.md";
  slug: "library/tehtris";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/the-hive.md": {
	id: "library/the-hive.md";
  slug: "library/the-hive";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/tranco.md": {
	id: "library/tranco.md";
  slug: "library/tranco";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/trellix.md": {
	id: "library/trellix.md";
  slug: "library/trellix";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/triage.md": {
	id: "library/triage.md";
  slug: "library/triage";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/vade-cloud.md": {
	id: "library/vade-cloud.md";
  slug: "library/vade-cloud";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/vade-secure.md": {
	id: "library/vade-secure.md";
  slug: "library/vade-secure";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/virustotal.md": {
	id: "library/virustotal.md";
  slug: "library/virustotal";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/whois.md": {
	id: "library/whois.md";
  slug: "library/whois";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"library/withsecure.md": {
	id: "library/withsecure.md";
  slug: "library/withsecure";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
"monitor/dashboard.md": {
	id: "monitor/dashboard.md";
  slug: "monitor/dashboard";
  body: string;
  collection: "docs";
  data: InferEntrySchema<"docs">
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	type ContentConfig = typeof import("../src/content/config");
}
