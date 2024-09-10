import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/_client/blog')({
  component: () => <div>Hello /_client/blog!</div>
})