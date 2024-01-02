<template>
  <q-dialog class="q-pa-lg">
    <div class="text-h6">Create a new chore</div>
    <q-separator inset />
    <q-form @submit="submitForm">
      <q-input
        label="Name"
        v-model="formState.name"
      ></q-input>
      <q-input
        label="Frequency"
        hint="How often (in days) would you like to do that?"
        v-model="formState.frequency"
      ></q-input>
      <q-input
        v-model="formState.lastCompletedAt"
        mask="date"
        :rules="['date']"
        label="Last completed at"
        hint="When did you last do it?"
      >
        <template v-slot:append>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="formState.lastCompletedAt">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>
      <q-btn flat>Cancel</q-btn>
      <q-btn color="primary" type="submit">Create</q-btn>
    </q-form>
  </q-dialog>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const emptyForm = {
  name: '',
  group: '',
  frequency: '',
  lastCompletedAt: ''
}

const formState = reactive({ ...emptyForm })

const choreAdded = ref(false)

function submitForm () {
  api.post(
    'chores/create/',
    {
      name: formState.name,
      completion_frequency: formState.frequency,
      last_completed_at: formState.lastCompletedAt,
      group_id: formState.group.value
    })
    .then(() => { choreAdded.value = true })
    .catch((error) => {
      const errorMessages = Object.values(error.response.data).join(',')
      $q.notify(
        { message: `Could not create a chore: ${errorMessages}` }
      )
    })
}

</script>
