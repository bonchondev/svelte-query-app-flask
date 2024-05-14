<script lang="ts">
    import { Response } from "$lib/data";
    import { route, zodFetch } from "$lib/query";
    import { createQuery } from "@tanstack/svelte-query";
    const query = createQuery({
        queryKey: ["data"],
        queryFn: async () =>
            await zodFetch(Response, route("docs"), {
                method: "GET",
                headers: { "Content-Type": "application/json" },
            }),
    });
</script>

<section class="py-4 px-5 flex flex-col gap-y-4">
    <h1 class="font-bold text-red-600 text-5xl">Data fetching</h1>
    <p class="font-bold text-3xl">Documents</p>
    {#if $query.isLoading}
        <span>Loading...</span>
    {:else if $query.isSuccess}
        {#each $query.data.documents as docs}
            <a href={`${route("output")}/${docs}`}>
                <p class="text-blue-700 font-semibold underline">{docs}</p>
            </a>
        {/each}
    {:else if $query.isError}
        <span>{$query.error}</span>
    {/if}
</section>
