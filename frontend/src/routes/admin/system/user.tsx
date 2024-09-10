import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/system/user')({
  component: () => <div>Hello /admin/system/user!</div>
})