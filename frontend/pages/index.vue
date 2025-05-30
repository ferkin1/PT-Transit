<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Search Popular Destinations</h1>
    <div class="flex gap-2 mb-4">
      <input v-model="origin" placeholder="e.g. LAX" class="border px-3 py-2 rounded" />
      <button @click="fetchDestinations" class="bg-blue-600 text-white px-4 py-2 rounded">
        Go
      </button>
    </div>
    <ul v-if="destinations.length">
      <li v-for="d in destinations" :key="d">
        {{ d.origin }} → {{ d.destination }} (€{{ d.Total_Score }})
      </li>
    </ul>
    <div v-if="!destinations.lengt">
      hello there !
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const origin = ref('MAD')
const destinations = ref([])

async function fetchDestinations() {
  const res = await fetch(`http://localhost:8000/api/get-popular-travel?origin=${origin.value}`, {
    headers: {
      "ngrok-skip-browser-warning": true,
      "Content-Type": "application/json"
    }
  })
  destinations.value = await res.json();
}
</script>