<template>
  <q-page class="q-pa-lg">
    <q-list bordered class="rounded-borders">
      <q-expansion-item
        expand-separator
        v-for="group in availableGroups"
        :key="group.label"
        :class="`chore-${group.status}`"
        class="rounded-borders q-ma-sm"
        v-model="group.expanded"
      >
        <template v-slot:header>
          <q-item-section class="row items-center">{{ group.label }}</q-item-section>
        </template>
        <q-card>
            <div class="q-pa-md">
              <div class="q-gutter-x-xl q-gutter-y-xl">
                <ChoreCard
                  :chore="chore"
                  @chore-updated="refreshGroups"
                  v-for="chore in group.chores"
                  :key="chore.id"
                />
              </div>
            </div>
        </q-card>
      </q-expansion-item>
    </q-list>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { useQuasar } from 'quasar'
import { getAllGroups, statusOrderer } from 'helpers/choreGroups'
import ChoreCard from 'components/ChoreCard'

const $q = useQuasar()

const availableGroups = ref(null)
refreshGroups()

function refreshGroups () {
  getAllGroups()
    .then(
      (data) => {
        availableGroups.value = data.filter((group) => group.chores.length > 0)
        availableGroups.value.sort(statusOrderer)
      }
    )
    .catch((error) => {
      const errorMessages = Object.values(error).join(',')
      $q.notify(
        { message: `Could not fetch available groups: ${errorMessages}` }
      )
    })
}

</script>
