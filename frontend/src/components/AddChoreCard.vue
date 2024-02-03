<template>
  <div>
    <q-btn class="chore chore-add" @click="showAddDialog = true">
      Add a new chore
      <q-icon name="add_circle_outline"/>
    </q-btn>
    <q-dialog v-model="showAddDialog" class="q-pa-lg" no-backdrop-dismiss>
      <div class="column q-pa-sm dark-bgr">
        <h5 class="q-my-md col text-center">Add a new chore</h5>
        <q-form class="q-mt-none q-mx-lg col" @submit="submitForm">
          <q-input
            label="Name"
            v-model="formState.name"
            :rules="[val => !!val || 'Field is required']"
          ></q-input>
          <q-input
            label="Frequency (days)"
            v-model="formState.frequency"
            type="number"
            :rules="[val => !!val || 'Field is required']"
          ></q-input>
          <q-input
            v-model="formState.lastCompletedAt"
            mask="date"
            :rules="['date']"
            label="Last completed at"
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
          <q-btn flat v-close-popup class="q-ma-sm">Cancel</q-btn>
          <q-btn v-close-popup class="q-ma-sm" color="primary" type="submit">Create</q-btn>
        </q-form>
      </div>
    </q-dialog>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'

const emit = defineEmits(['choreAdded'])
const props = defineProps({
  choreGroupId: {
    type: String,
    required: true
  }
})

const $q = useQuasar()

const showAddDialog = ref(false)

const emptyForm = {
  name: '',
  frequency: '',
  lastCompletedAt: ''
}
let formState = reactive({ ...emptyForm })

function submitForm () {
  api.post(
    'chores/create/',
    {
      name: formState.name,
      completion_frequency: formState.frequency,
      last_completed_at: formState.lastCompletedAt,
      group_id: props.choreGroupId
    })
    .then(() => {
      emit('choreAdded')
      formState = { ...emptyForm }
    })
    .catch((error) => {
      const errorMessages = Object.values(error.response.data).join(',')
      $q.notify(
        { message: `Could not create a chore: ${errorMessages}` }
      )
    })
}
</script>

<style lang="scss" scoped>
.chore-add {
   background-color: beige;
}

.dark-bgr {
  background-color: $green-1;
}
</style>
