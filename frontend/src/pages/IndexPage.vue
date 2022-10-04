<template>
  <q-page class="q-pa-lg">
    <q-list bordered class="rounded-borders">
      <q-expansion-item
        expand-separator
        v-for="group in availableGroups"
        :key="group.label"
        :class="`chore-${group.status}`"
      >
        <template v-slot:header>
          <q-item-section class="row items-center">{{ group.label }}</q-item-section>
        </template>
        <q-card>
            <div class="q-pa-md">
              <div class="q-gutter-x-md q-gutter-y-lg">
                <ChoreCard :chore="chore" v-for="chore in group.chores" :key="chore.id" />
              </div>
            </div>
        </q-card>
      </q-expansion-item>
    </q-list>
  </q-page>
</template>

<script setup>
import { getAllGroups } from 'helpers/api'
import ChoreCard from 'components/ChoreCard'

const availableGroups = getAllGroups()

// TODO add default-opened jeśli status jest na czerwono
// TODO: ordering po statusie

</script>
