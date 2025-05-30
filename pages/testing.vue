<script setup>

import { ref } from 'vue'

const topRow = ref([]);

async function loadData() {
  const res = await fetch('https://9812-216-9-21-115.ngrok-free.app/api/get-popular-travel?origin=MAD', {
    headers: {
      "ngrok-skip-browser-warning": true,
      "Content-Type": "application/json"
    }
  });
  topRow.value = await res.json();
}

</script>

<template>
  <div class="p-6">
    <button @click="loadData" class="bg-blue-600 text-white px-4 py-2 rounded">Fetch Destinations</button>
    <div v-if="!topRow">
      <IconsSpinner />
    </div>
    <div v-else>
      <table>
        <thead>
        <tr>
          <th>#</th>
          <th>type</th>
          <th>destination</th>
          <th>subType</th>
          <th>Total Score</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(row, index) in topRow" :key="index">
          <td class="padding-td">{{ index }}</td>
          <td class="padding-td">{{ row.type }}</td>
          <td class="padding-td">{{ row.destination }}</td>
          <td class="padding-td">{{ row.subType }}</td>
          <td class="padding-td">{{ row.Total_Score }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>