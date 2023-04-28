import { api } from 'boot/axios'

export async function getAllGroups () {
  const response = await api.get('chores/groups/')
  return response.data.map(x => ({
    label: x.name,
    value: x.id,
    status: x.status,
    chores: x.chores
  }))
}
