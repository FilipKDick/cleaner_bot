<template>
  <q-page class="column items-center justify-center">
    <q-card class="create-chore-card q-pa-lg">
      <q-form @submit="submitForm">
        <q-card-section>
          <div class="text-h6">Create a new chore</div>
        </q-card-section>
        <q-separator inset />
        <q-card-section class="column q-gutter-md">
          <q-input
            label="Name"
            v-model="formState.name"
          ></q-input>
          <q-select
            label="Chore group"
            v-model="formState.group"
            :options="availableGroups"
            bottom-slots
          >
          <template v-slot:hint>
            <div>Your group not there? You can <a href=https://example.com>Add a new group</a></div>
          </template>
          </q-select>
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
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat>Cancel</q-btn>
          <q-btn color="primary" type="submit">Create</q-btn>
        </q-card-actions>
      </q-form>
    </q-card>
  </q-page>
  <q-dialog v-model="choreAdded">
    <q-card>
      <q-card-section>
        <div class="text-h6">Chore added successfully!</div>
      </q-card-section>

      <q-card-actions align="right">
        <q-btn flat label="See it in group" color="primary" v-close-popup @click="todo"/>
        <q-btn flat label="Add another one" color="primary" v-close-popup @click="todo"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'
import { getAllGroups } from 'helpers/api'

const $q = useQuasar()

const formState = reactive({
  name: '',
  group: '',
  frequency: '',
  lastCompletedAt: ''
})

const choreAdded = ref(false)
const availableGroups = getAllGroups()

function submitForm () {
  console.log('formState', formState)
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

function todo () {
  // TODO: fill this function
  console.log('https://example.com')
}
</script>

<style lang="scss">
.create-account-card {
  width: 512px;
}

.password-criteria {
  background-color: #efefef;
  border-radius: 0.5rem;
}
</style>
