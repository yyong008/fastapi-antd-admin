import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/_client/news')({
  component: () => <div>Hello /_client/news!</div>
})