<template>
  <q-page class="column items-center justify-center">
    <q-card class="create-chore-group-card q-pa-lg">
      <q-form @submit="submitForm">
        <q-card-section>
          <div class="text-h6">Create a new chore group</div>
        </q-card-section>
        <q-separator inset />
        <q-card-section class="column q-gutter-md">
          <q-input
            label="Name"
            v-model="formState.name"
          ></q-input>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat>Cancel</q-btn>
          <q-btn color="primary" type="submit">Create</q-btn>
        </q-card-actions>
      </q-form>
    </q-card>
  </q-page>
  <q-dialog v-model="choreGroupAdded">
    <q-card>
      <q-card-section>
        <div class="text-h6">Chore added successfully!</div>
      </q-card-section>

      <q-card-actions align="right">
        <!--        TODO: auto-select newly added group (get param) -->
        <q-btn flat label="Add chores to it" color="primary" v-close-popup :to="{name: 'addChore' }"/>
        <q-btn flat label="Add another one" color="primary" v-close-popup @click="clearForm"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'

const $q = useQuasar()

const emptyForm = {
  name: ''
}

const formState = reactive({ ...emptyForm })

const choreGroupAdded = ref(false)

function submitForm () {
  api.post('chores/groups/', { name: formState.name })
    .then(() => { choreGroupAdded.value = true })
    .catch((error) => {
      const errorMessages = Object.values(error.response.data).join(',')
      $q.notify(
        { message: `Could not create a chore group: ${errorMessages}` }
      )
    })
}

function clearForm () {
  Object.assign(formState, emptyForm)
}

</script>
