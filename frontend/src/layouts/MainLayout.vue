<template>
  <q-layout view="hhh lpR fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />
        <q-toolbar-title>
          <q-avatar>
            <img src="~assets/logo.jpg">
          </q-avatar>
          Cleaner Bot
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <SidebarLink
          v-for="link in links"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import SidebarLink from 'components/SidebarLink.vue'

const linksList = [
  {
    title: 'See all chores',
    icon: 'assignment',
    link: 'allChores'
  },
  {
    title: 'Add a new chore',
    icon: 'add_task',
    link: 'addChore'
  },
  {
    title: 'Add a new chore group',
    icon: 'add_circle_outline',
    // TODO:
    link: 'https://example.com'
  }
]

export default defineComponent({
  name: 'MainLayout',

  components: {
    SidebarLink
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      links: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
