import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/blog/edit')({
  component: () => <div>Hello /admin/blog/edit!</div>
})