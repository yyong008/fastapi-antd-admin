import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/dashboard/')({
  component: () => <div>Hello /_admin/dashboard!</div>
})