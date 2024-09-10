import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/_admin')({
  component: () => <div>Hello /_admin!</div>
})