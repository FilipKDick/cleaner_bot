<template>
  <div>
    <q-btn
      class="chore"
      @click="showAddDialog = true"
    >
      Add a new chore
      <q-icon name="add_circle_outline" size="70px"/>
    </q-btn>
    <AddChoreDialog
      v-if="showAddDialog"
      @chore-added="emit('choreAdded')"
    />
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
import AddChoreDialog from 'components/AddChoreDialog.vue'

const emit = defineEmits(['choreAdded'])

const showAddDialog = ref(false)

</script>

<style lang="scss" scoped>
.chore {
   height:170px;
   width:170px;
   cursor:pointer;
   border-radius: 10%;
   background-color: beige;
}

</style>
