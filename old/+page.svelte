<script>
    import { onMount } from 'svelte';

    let count = 0;

    function increment() {
        count++;
    }

    let downhill = 0;
    let uphill = 0;
    let length = 0;

    let prediction = "n.a.";
    let din33466 = "n.a.";
    let sac = "n.a.";

    onMount(() => {
        if (browser) {
            // Diese Zeilen werden nur im Browser ausgeführt, nicht während SSR
            url = location.protocol + '//' + location.host;
        } else {
            // SSR oder Entwicklungsserver
            url = "http://localhost:5000";
        }
    });

    async function predict() {
        const response = await fetch(`${url}/api/predict?` + new URLSearchParams({
            downhill,
            uphill,
            length
        }));
        const data = await response.json();
        prediction = data.time;
        din33466 = data.din33466;
        sac = data.sac;
    }
</script>

<div class="container-fluid">

<h1>HikePlanner</h1>
<p>
    Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
</p>

<button on:click={increment}>
    Clicked {count}
    {count === 1 ? "time" : "times"}
</button>

<p>
    <strong>Abwärts [m]</strong>
    <label>
        <input type="number" bind:value={downhill} min="0" max="10000" />
        <input type="range" bind:value={downhill} min="0" max="10000" />
    </label>
</p>

<p>
    <strong>Aufwärts [m]</strong>
    <label>
        <input type="number" bind:value={uphill} min="0" max="10000" />
        <input type="range" bind:value={uphill} min="0" max="10000" />
    </label>
</p>

<p>
    <strong>Distanz [m]</strong>
    <label>
        <input type="number" bind:value={length} min="0" max="30000" />
        <input type="range" bind:value={length} min="0" max="30000" />
    </label>
</p>

<button on:click={predict}>Predict</button>

<p></p>
<table>
    <tr>
        <td>Dauer:</td><td>{prediction}</td>
    </tr>
    <tr>
        <td>DIN33466:</td><td>{din33466}</td>
    </tr>
    <tr>
        <td>SAC:</td><td>{sac}</td>
    </tr>
</table>

</div>

