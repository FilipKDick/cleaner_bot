import { api } from 'boot/axios'
import { useQuasar } from 'quasar'
import { ref } from 'vue'

export function getAllGroups () {
  const $q = useQuasar()
  const availableGroups = ref(null)
  api.get('chores/groups/')
    .then((response) => {
      availableGroups.value = response.data.map(x => ({
        label: x.name,
        value: x.id,
        status: x.status,
        chores: x.chores
      }))
    })
    .catch((error) => {
      const errorMessages = Object.values(error.response.data).join(',')
      $q.notify(
        { message: `Could not fetch available groups: ${errorMessages}` }
      )
    })
  return availableGroups
}
