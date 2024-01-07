<template>
  <div>
    <q-btn class="group q-mx-sm" @click="showAddDialog = true">
      <q-icon class="q-mx-md" name="add_circle_outline" size="40px"/>
      Add a new group
    </q-btn>
    <q-dialog v-model="showAddDialog" class="q-pa-lg" no-backdrop-dismiss>
      <div class="column q-pa-sm dark-bgr">
        <h5 class="q-my-md col text-center">Add a new group</h5>
        <q-form class="q-mt-none q-mx-lg col" @submit="submitForm">
          <q-input
            label="Name"
            v-model="formState.name"
            :rules="[val => !!val || 'Field is required']"
          ></q-input>
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

const emit = defineEmits(['groupAdded'])

const $q = useQuasar()

const showAddDialog = ref(false)

const emptyForm = {
  name: ''
}
let formState = reactive({ ...emptyForm })

function submitForm () {
  api.post('chores/groups/', { name: formState.name })
    .then(() => {
      emit('groupAdded')
      formState = { ...emptyForm }
    })
    .catch((error) => {
      const errorMessages = Object.values(error.response.data).join(',')
      $q.notify(
        { message: `Could not create group: ${errorMessages}` }
      )
    })
}
</script>

<style lang="scss" scoped>
.group {
  font-size: 14px;
   height: 3.42em;
   width: calc(100% - 16px);
   background-color: beige;
   font-weight: normal;
}

.dark-bgr {
  background-color: $green-1;
}
</style>
