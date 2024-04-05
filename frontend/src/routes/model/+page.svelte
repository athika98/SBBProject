<script>
    import { writable } from "svelte/store";
    // Erstelle die reaktiven Variablen
    const plz = writable("");
    const einwohnerzahl = writable("");

    // Erstelle eine reaktive Variable für die Vorhersageergebnisse
    let vorhersageErgebnis = "";

    // Funktion zum Senden der Daten und Empfangen der Vorhersage vom Backend
    async function handleSubmit() {
        const payload = {
            plz: $plz,
            einwohnerzahl: $einwohnerzahl,
        };

        try {
            const response = await fetch("http://localhost:5000/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
            });

            if (!response.ok) {
                throw new Error(
                    `Fehler beim Senden der Anfrage - HTTP-Fehler: Status ${response.status}`,
                );
            }

            const result = await response.json();
            vorhersageErgebnis = `Die Vorhersage für die Postleitzahl ist wie folgt - GA-Abonnements: ${result.GA}, Halbtax-Abonnements: ${result.Halbtax}.`;
        } catch (error) {
            vorhersageErgebnis = `Fehler bei der Anfrage: ${error.message}`;
        }
    }
</script>

<div class="container-fluid">
    <h2>Anzahl GA und HA in einem Gebiet berechnen</h2>
    <br />
    <div class="container-fluid custom-container">
        <!--div class="row">
            <div class="col-4 align-self-start">
                <div class="mb-3">
                    <label for="gaorha" class="form-label"> Was möchtest du berechnen?</label>
                </div>
            </div>
            <div class="col-4 align-self-start">
                <div class="mb-3">
                    <select class="form-select" bind:value={$auswahl}>
                        <option selected>Wählen</option>
                        <option value="GA">GA</option>
                        <option value="Halbtax">Halbtax</option>
                        <option value="Beide">Beides</option>
                    </select>
                </div>
            </div>
        </div-->
        <div class="row">
            <div class="col-4 align-self-start">
                <div class="mb-3">
                    <label for="plz" class="form-label"
                        >Postleitzahl eingeben</label
                    >
                </div>
            </div>
            <div class="col-4 align-self-start">
                <div class="mb-3">
                    <input
                        type="text"
                        class="form-control"
                        id="plz"
                        placeholder="8004"
                        bind:value={$plz}
                    />
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-4 align-self-start">
                <div class="mb-3">
                    <label for="einwohnerzahl" class="form-label"
                        >Anzahl Einwohner eingeben</label
                    >
                </div>
            </div>
            <div class="col-4 align-self-start">
                <div class="mb-3">
                    <input
                        type="text"
                        class="form-control"
                        id="einwohnerzahl"
                        placeholder="10000"
                        bind:value={$einwohnerzahl}
                    />
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-4 align-self-start">
            <div class="mb-3"></div>
        </div>
        <div class="col-4 align-self-start">
            <div class="mb-3">
                <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                    <button
                        on:click={handleSubmit}
                        type="button"
                        class="btn button-calculate">Berechnen</button
                    >
                </div>
            </div>
        </div>
    </div>

    <h3>Vorhersage</h3>
    <p>{vorhersageErgebnis}</p>
</div>

<style>
    .container-fluid {
        padding-left: 20px;
    }
    .custom-container {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    .button-calculate {
        background-color: MistyRose;
        border-color: lightpink;
    }
</style>
