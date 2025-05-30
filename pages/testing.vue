<script setup>
const topRow = ref(null);

async function loadData() {
  const res = await $fetch('/api/get-popular-travel?origin=MAD');
  topRow.value = await res;
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
        <tr v-for="(row, index) in topRow.data" :key="index">
          <td class="padding-td">{{ index }}</td>
          <td class="padding-td">{{ row.type }}</td>
          <td class="padding-td">{{ row.destination }}</td>
          <td class="padding-td">{{ row.subType }}</td>
          <td class="padding-td">{{ row.analytics.flights.score + row.analytics.travelers.score }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>