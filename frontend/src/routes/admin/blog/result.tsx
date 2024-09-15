import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin/blog/result')({
  component: () => <div>Hello /admin/blog/result!</div>
})