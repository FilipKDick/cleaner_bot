import { api } from 'boot/axios'

export async function getAllGroups () {
  const response = await api.get('chores/groups/')
  return response.data.map(x => ({
    label: x.name,
    value: x.id,
    status: x.status,
    chores: x.chores,
    expanded: x.status === 'overdue' // TODO: due?
  }))
}

export function statusOrderer (a, b) {
  const statusOrder = {
    overdue: 1,
    due: 2,
    soon: 3,
    safe: 4
  }

  const statusA = statusOrder[a.status]
  const statusB = statusOrder[b.status]

  if (statusA < statusB) {
    return -1
  } else if (statusA > statusB) {
    return 1
  } else {
    return 0
  }
}
