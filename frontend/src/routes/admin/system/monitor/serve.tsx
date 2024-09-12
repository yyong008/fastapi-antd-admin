import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/system/monitor/serve')({
  component: () => <div>Hello /admin/system/monitor/serve!</div>
})