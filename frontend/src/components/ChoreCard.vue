<template>
  <q-btn
    class="chore"
    @click="setDone()"
    :class="`chore-${chore.status}`"
  >
    {{ chore.name }} <br><br>
    {{ choreComment() }}
  </q-btn>
</template>

<script setup>
import { defineProps, ref } from 'vue'
import { api } from 'boot/axios'

const props = defineProps(['chore'])
const chore = ref(props.chore)

function setDone () {
  api.post(
    'chores/',
    {}
  )
}

function choreComment () {
  if ((chore.value.status === 'safe') | (chore.value.status === 'soon')) {
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
