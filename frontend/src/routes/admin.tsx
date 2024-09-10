import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/admin')({
  component: () => <div>Hello /_admin!</div>
})