<template>
  <q-btn
    class="chore"
    @click="setDone()"
    :class="`chore-${choreStatus}`"
  >
    {{ chore.name }} <br><br>
    {{ choreComment() }}
  </q-btn>
</template>

<script setup>
import { defineEmits, defineProps, ref } from 'vue'
import { useQuasar } from 'quasar'
import { api } from 'boot/axios'

const props = defineProps(['chore'])
const emit = defineEmits(['choreUpdated'])
const chore = ref(props.chore)
const choreStatus = ref(chore.value.status)

const $q = useQuasar()

function setDone () {
  api.post(
    'chores/mark_done/',
    { chore_id: chore.value.id }
  )
    .then((resp) => {
      choreStatus.value = 'safe'
      chore.value = resp.data
      emit('choreUpdated')
    }
    )
    .catch((error) => {
      const errorMessages = Object.values(error.response.data).join(',')
      $q.notify(
        { message: `Could not mark as done: ${errorMessages}` }
      )
    })
}

function choreComment () {
  if ((chore.value.status === 'safe') || (chore.value.status === 'soon')) {
    return `Should be done at ${chore.value.due_date}`
  }
  return `Should've been done before ${chore.value.due_date}`
}
</script>

<style lang="scss">
.chore {
   height:200px;
   width:200px;
   cursor:pointer;
}

</style>
