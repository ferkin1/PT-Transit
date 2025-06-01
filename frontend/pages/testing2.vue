<template>
  <div class="max-w-xl mx-auto p-6">
    <h1 class="text-2xl font-bold mb-4">🔍 Search Popular Destinations</h1>

    <!-- 1) Input + button -->
    <div class="flex mb-4 gap-2">
      <input
          v-model="origin"
          placeholder="Enter origin (e.g. MAD)"
          class="flex-1 border px-3 py-2 rounded"
      />
      <button
          @click="fetchDestinations"
          :disabled="loading"
          class="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
      >
        {{ loading ? 'Loading…' : 'Search' }}
      </button>
    </div>

    <!-- 2) Error -->
    <p v-if="error" class="text-red-600 mb-4">{{ error }}</p>

    <!-- 3) Results -->
    <ul v-if="destinations.length" class="space-y-2">
      <li
          v-for="(d, i) in destinations"
          :key="i"
          class="bg-black border rounded shadow p-4 flex justify-between"
      >
        <span>✈️ {{ d.origin }} → {{ d.destination }}</span>
        <span class="font-semibold">€{{ d.Total_Score }}</span>
      </li>
    </ul>

    <!-- 4) Empty state -->
    <p v-else-if="!loading && !error" class="text-gray-600">
      No destinations loaded yet.
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const origin       = ref('MAD')
const destinations = ref([])
const loading      = ref(false)
const error        = ref('')

async function fetchDestinations() {
  loading.value = true
  error.value   = ''
  destinations.value = []

  try {
    // If you have a Vite proxy set up in nuxt.config.ts to forward /api → your FastAPI:
    const url = `http://localhost:8000/api/get-popular-travel?origins=${origin.value}`

    // Otherwise, call the full backend URL:
    // const url = `http://localhost:8000/api/get-popular-travel?origins=${origin.value}`

    const res = await fetch(url, {
      headers: {
        "ngrok-skip-browser-warning": true,
        "Content-Type": "application/json"
      }
    })
    if (!res.ok) {
      throw new Error(`Server returned ${res.status}`)
    }
    // your FastAPI returns a JSON array of { origin, destination, price, … }
    destinations.value = await res.json()
  } catch (e) {
    console.error(e)
    error.value = e.message || 'Failed to load data'
  } finally {
    loading.value = false
  }
}
</script>