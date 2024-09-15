import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/blog/edit/$id')({
  component: () => <div>Hello /admin/blog/create!</div>
})