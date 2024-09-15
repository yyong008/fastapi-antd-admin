import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/blog/tag')({
  component: () => <div>Hello /admin/blog/tag!</div>
})